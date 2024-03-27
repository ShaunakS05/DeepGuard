import re
from urllib.parse import urlparse, parse_qs
import whois
import tldextract
from datetime import datetime
import ssl
import socket
from OpenSSL import crypto

def is_ad_domain(url):
    # Function to check if the URL is an ad domain
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    ad_indicators = ['utm_source', 'utm_medium', 'clickid', 'aff', 'affiliate']
    if any(param in query_params for param in ad_indicators):
        return True
    ad_domain_indicators = ['ads', 'banner', 'sponsor', 'affiliate']
    if any(indicator in parsed_url.netloc for indicator in ad_domain_indicators):
        return True
    if any(indicator in url for indicator in ad_domain_indicators):
        return True
    return False

def is_irrelevant_domain(url):
    # List of irrelevant indicators
    irrelevant_indicators = ['/login', '/register', '/subscribe', '#', 'mailto:', 'javascript:']
    
    # Check if URL is irrelevant based on indicators
    if any(indicator in url for indicator in irrelevant_indicators):
        return True
    
    # Check if URL is a downloadable file type, often considered irrelevant for content scraping
    if url.endswith(('.pdf', '.doc', '.docx', '.mp3', '.mp4')):
        return True

    # If none of the above conditions are met, the URL is not considered irrelevant
    return False

def is_valid_domain(domain):
    # Define what makes a domain "valid"
    minimum_age_years = 1  # You can change this as per your requirement
    trusted_tlds = ['gov', 'edu', 'org', 'com']  # Considered as trusted TLDs

    # Extract the base domain using tldextract
    base_domain = tldextract.extract(domain).registered_domain

    # Get the domain's WHOIS information
    domain_info = whois.whois(base_domain)

    # Analyze domain age (older domains might be more credible)
    creation_date = domain_info.creation_date
    if isinstance(creation_date, list):  # Handling the case where creation_date is a list
        creation_date = creation_date[0]
    age_years = (datetime.now() - creation_date).days / 365.25  # Convert age to years

    # Check if the domain is using a generally trusted TLD
    is_trusted_tld = tldextract.extract(domain).suffix in trusted_tlds

    # Decide if the domain is "valid" based on age and TLD
    is_valid = age_years >= minimum_age_years and is_trusted_tld

    return is_valid

def verify_ssl_certificate(url_or_domain, port=443):
    # Extract domain name from URL if necessary
    if "//" in url_or_domain:
        domain_name = url_or_domain.split("//")[-1].split("/")[0]
    else:
        domain_name = url_or_domain
    
    # Create a default context that checks hostname and CA
    context = ssl.create_default_context()

    try:
        with socket.create_connection((domain_name, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain_name) as ssock:
                # Retrieve the certificate in DER format
                der_cert = ssock.getpeercert(binary_form=True)
                # Convert to X509 object
                cert = crypto.load_certificate(crypto.FILETYPE_ASN1, der_cert)
                
                # Check if the certificate is expired
                not_after = datetime.strptime(cert.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
                not_before = datetime.strptime(cert.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
                current_time = datetime.utcnow()
                if current_time > not_after or current_time < not_before:
                    return False, "The certificate is expired or not yet valid."
                    
                return True, "The certificate is valid."

    except ssl.CertificateError as e:
        return False, f"Certificate error: {e}"
    except ssl.SSLError as e:
        return False, f"SSL error: {e}"
    except Exception as e:  # Catch other possible exceptions
        return False, f"Unexpected error: {e}"

# # Test the function with both a URL and a domain name
# url = 'https://www.supremecourt.gov/opinions/23pdf/23-719_19m2.pdf'
# is_valid, message = verify_ssl_certificate(url)
# print(f"Validation result: {is_valid}, Message: {message}")



# url = "google.com"
# if(verify_ssl_certificate(url)):
#     print("The certificate is valid!")


def filter_domains(domains):
    # Function to filter out unwanted domains
    filtered_domains = []
    for domain in domains:
        if not is_ad_domain(domain) and not is_irrelevant_domain(domain):
            if is_valid_domain(domain) and verify_ssl_certificate(domain):
                filtered_domains.append(domain)
    return filtered_domains

# Example usage
# original_domains = ['https://example.com/login', 'https://example.com/content', 
#                   'https://ads.example.com/click', 'https://example.com/download.pdf', 
#                   'https://example.com#section', 'https://external.com']
# filtered_domains = filter_domains(original_domains)
# print(filtered_domains)
