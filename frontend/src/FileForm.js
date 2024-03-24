import './App.css'
import {React, useState} from 'react';

function FileForm()
{
    const[file, setFile] = useState(null);
    const handle = (event) => {
        setFile(event.target.files[0])
    }
    const handleSubmit = (event) => {
        event.preventDefault();

        const formData = new FormData();
        formData.append("file_upload")

    }
    return(
        <div>
            <h1>Upload File</h1>
                <form onSubmit={handleSubmit}>
                    <div>
                        <input type="file" onChange={handle}></input>
                        <button type="submit"> Upload </button>
                    </div>
                </form>
                {file && <p>{file.name}</p>}
        </div>
    )
}
export default FileForm; 