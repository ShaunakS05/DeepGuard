import ssl
import socket
from datetime import datetime
from OpenSSL import crypto

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

# Test the function with both a URL and a domain name
url = 'https://www.supremecourt.gov/opinions/23pdf/23-719_19m2.pdf'
is_valid, message = verify_ssl_certificate(url)
print(f"Validation result: {is_valid}, Message: {message}")

