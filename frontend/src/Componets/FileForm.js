import {useState, React}from "react"



function FileForm() {

    const[file,setFile] = useState(null);

    const handleFileInputChange = (event) => {
        setFile(event.target.files[0])
    }
    return (
        <p>f</p>
    )

}
export default FileForm;