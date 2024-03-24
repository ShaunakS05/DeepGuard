import './App.css';
import bg from './cool-background.svg';
import bg2 from './cool-background2.png';
import bg3 from './cool-background3.png';
import gsap from "gsap";
import React, { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import FileForm from './Componets/FileForm';
import SplitTextJS from 'split-text-js';
import Button from 'react-bootstrap/Button';




function App() {

  const endpoint_Visual = "http://localhost:8000/check-visual-deepfake"
  const endpoint_Audio = "http://localhost:8000/check-audio-deepfake"
  const endpoint_Text = "http://localhost:8000/check-text-deepfake" 

  const endpoint_TTYT = "http://localhost:8000/title/"
  const endpoint_picture = "http://localhost:8000/thumbnail/"

  const[vis, setVis] = useState(null);
  const[file, setFile] = useState(null);

  const[useVisual, setVisual] = useState(false);
  const[useAudio, setAudio] = useState(false);
  const[useText, setText] = useState(false);

  const[name, setName] = useState(null);
  const[context, setContext] = useState(null);

  const[text_score, setTextScore] = useState(null);
  const[Text_explanation1, setTextExplanation] = useState(null);

  const[visualData, setVisData] = useState(null);
  const[audioData, setAudData] = useState(null);
  const[textData, setTexData] = useState(null);

  const[ytLink, setYTlink] = useState(null);
  const[useYoutube, setYoutubeCheck] = useState(null);


  const [isChecke1d, setIsChecke1d] = useState(false);

  const [isChecked, setIsChecked] = useState(false);

  const[ytTitle, setYTtitle] = useState(null);
  const[ytImage, setYtImage] = useState(null);



  const handleFileChange = (event) => {
    setFile(event.target.files[0])
  }

  const handleDetect = async (event) => {
    setIsChecke1d(true);
    event.preventDefault();
    if(useVisual)
    {
      const formData = new FormData();
      formData.append('file_upload', file);
      try {
  
        const response = await fetch(endpoint_Visual, {
          method: "POST",
          body: formData
        });
    
        // Check if the response status is OK (200)
        if (response.ok) {
          // Try to parse the response as JSON
          const response_data = await response.json();
          const outputObject = JSON.parse(response_data)
          const resultValue = outputObject.result
          console.log(response)
          console.log("Success YIPPEEE" + response_data)
          console.log("Success YIPPEEE" + resultValue)
          // Now you can use the response data as needed
          setVisData(resultValue);
        } else {
          // If response status is not OK, throw an error
          throw new Error('Failed tozsasd fetch data');
        }
          
      }
      catch(error)
      {
        console.error(error);
      }
    }
    if(useText)
    {
      const formDataText = new FormData();
      formDataText.append('file_upload', file);
      formDataText.append('name', name);
      formDataText.append('context', context);

      try {
  
        const response = await fetch(endpoint_Text, {
          method: "POST",
          body: formDataText
        });
    
        // Check if the response status is OK (200)
        if (response.ok) {
          const response_data = await response.json();
          // Try to parse the response as JSON
          //const response_data = await response.json();
          const outputObject = JSON.parse(response_data);
          //const outputObject = JSON.parse(response_data)
          //const Text_Score = outputObject.numerical_answer
          //const Text_explanation = outputObject.explanation
          //setTextScore(Text_Score);
          //setTextExplanation(Text_explanation);
          //console.log(response)
          console.log("Success YIPPEEE" + outputObject.numerical_answer)
          console.log("Success YIPPEEE" + outputObject.explanation)
          // Now you can use the response data as needed
          setVisData(outputObject.numerical_answer);
        } else {
          // If response status is not OK, throw an error
          throw new Error('Failed tozsasd fetch data');
        }
          
      }
      catch(error)
      {
        console.error(error);
      }}
    
    if(useYoutube)
    {
      
        const YTData = new FormData();
        YTData.append('youtube_link', ytLink);
        try {
    
          const response = await fetch(endpoint_TTYT, {
            method: "POST",
            body: YTData
          });
      
          // Check if the response status is OK (200)
          if (response.ok) {
            // Try to parse the response as JSON

            const response_data = await response.json();
            console.log(response_data)
            setYTtitle(response_data);


            const outputObject = JSON.parse(response_data)
            const resultValue = outputObject.Title
            console.log(response)
            console.log("Success YIPPEEE" + response_data)
            console.log("Success YIPPEEE" + resultValue)
            // Now you can use the response data as needed
          } else {
            // If response status is not OK, throw an error
            throw new Error('Failed tozsasd fetch data');
          }
            
        }
        catch(error)
        {
          console.error(error);
        }
        try {
    
          const response = await fetch(endpoint_picture, {
            method: "POST",
            body: YTData
          });
      
          // Check if the response status is OK (200)
          if (response.ok) {
            // Try to parse the response as JSON

            const response_data = await response.json();
            console.log(response_data)
            setYtImage(response_data);


            const outputObject = JSON.parse(response_data)
            const resultValue = outputObject.Title
            console.log(response)
            console.log("Success YIPPEEE" + response_data)
            console.log("Success YIPPEEE" + resultValue)
            // Now you can use the response data as needed
          } else {
            // If response status is not OK, throw an error
            throw new Error('Failed tozsasd fetch data');
          }
            
        }
        catch(error)
        {
          console.error(error);
        }
      
    }
  }
  
  const handleClick = () => {
    alert('Button clicked!');
  };

  const handleName = (event) => {
    setName(event.target.value);
  }
  const handleContext = (event) => {
    setContext(event.target.value);
  }
  const handleVisualCheck = () => {
    setVisual(!useVisual);
  };
  const handleAudioCheck = () => {
    setAudio(!useAudio);
  };
  const handleText = () => {
    setText(!useText);
  };
  const handleTextYT = (event) => {
    setYTlink(event.target.value);
  };
  const handleYTCheck = () => {
    setYoutubeCheck(!useYoutube)
  };



  const onDrop = useCallback(acceptedFiles => {
    // Assuming you want to handle a single file, use the first file in the array
    setFile(acceptedFiles[0]);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });
  const titles = gsap.utils.toArray("p");
  const tl = gsap.timeline({repeat: -1, yoyo: true, repeatDelay: 1});

  titles.forEach(title => {
    const splitTitle = new SplitTextJS(title);

    tl
      .from(splitTitle.chars, {
        opacity: 0,
        y: 80,
        rotateX: 90,
        stagger: 0.02
      }, "<")
      .to(splitTitle.chars, {
        opacity: 0,
        y: -80,
        rotateX: 90,
        stagger: 0.02
      }, "<1")
  });




  return (

    <div className="App">
        <div style={{
        backgroundImage: `url(${bg})`,
        backgroundSize: 'cover', // Use '100% 100%' if you want to stretch the image to fill the container.
        width: '100vw', // Set the width to 100% of the viewport width
        height: '100vh', // Set the height to 100% of the viewport height
        backgroundPosition: 'center', // Center the background image
        backgroundRepeat: 'no-repeat', // Prevent the background image from repeating
      }}>
        <div className="title">
          Detecting Deepfakes Through:
          </div>
          <div class="container" >
              <p className='one'>Video</p>
              <p className='two'>Voice</p>
              <p className='three'>Text</p>
          </div>

        <div className='buttonPlace'>

        <Button className="coolBlueButton" onClick={handleClick}>Try Demo! </Button>

        </div>           
      </div>

      
      
      <div style={{
  position: 'relative',
  backgroundImage: `url(${bg3})`,
  width: '100vw',
  height: '100vh',
  // Other styling for the container
}}>
  <div style={{
    position: 'absolute',
    left: 'calc(33.33% - 200px)', // Moves the box to the left third and then 50px to the left
    top: '50%', // Adjust as needed
    transform: 'translateY(-50%)', // Centers the box vertically
    width: '300px', // Your box width
    height: '600px', // Your box height
    borderRadius: '40px',
    backgroundColor: 'white',
    // Other styling for the box
  }}>
     <div className="upload-section">
        <h1>Upload File</h1>
        <div {...getRootProps()} className="dropzone">
          <input {...getInputProps()} />
          {
            isDragActive ?
              <p>Drop the files here ...</p> :
              <p>Drag and Drop</p>
          }
                  {file && <p>File selected: {file.name}</p>}

        </div>
        </div>

    <textarea onChange={handleContext} value={context}
  className="cool-blue-textarea"
  placeholder="What is happening the video?"
    style={{position: 'absolute',
    left: 'calc(33.33% + 250px)', // Moves the box to the left third and then 50px to the left
    top: '20%', // Adjust as needed,
    transform: 'translateY(-50%)',
  }}
></textarea>
 
 <input type="text" className="cool-blue-input" 
    style={{position: 'absolute',
      left: 'calc(33.33% + 250px)', // Moves the box to the left third and then 50px to the left
      top: '5%', // Adjust as needed,
      width: '260px',
      transform: 'translateY(-50%)', // Centers the box vertically
 }} placeholder="Name of person..." onChange={handleName} value={name}/>


 
<input type="text" className="cool-blue-input" 
    style={{position: 'absolute',
      left: 'calc(33.33% + 250px)', // Moves the box to the left third and then 50px to the left
      top: '105%', // Adjust as needed,
      left: '0%',
      width: '260px',
      transform: 'translateY(-50%)', // Centers the box vertically
 }} placeholder="Link to Youtube Link" onChange={handleTextYT} value={ytLink}  />

  <div className='checkboxes'>
      <label>
        {/* The checkbox input */}
        <input
          type="checkbox"
          checked={useVisual}
          onChange={handleVisualCheck}
        />
        {/* Label text dynamically changes based on the checkbox state */}
        {isChecked ? 'Use Visual' : 'Use Visual'}
      </label>

      <label>
        {/* The checkbox input */}
        <input
          type="checkbox"
          checked={useAudio}
          onChange={handleAudioCheck}
        />
        {/* Label text dynamically changes based on the checkbox state */}
        {isChecked ? 'Use Audio' : 'Use Audio'}
      </label>

      <label>
        {/* The checkbox input */}
        <input
          type="checkbox"
          checked={useText}
          onChange={handleText}
        />
        {/* Label text dynamically changes based on the checkbox state */}
        {isChecked ? 'Use Text' : 'Use Text'}
      </label>
      <label>
        {/* The checkbox input */}
        <input
          type="checkbox"
          checked={useYoutube}
          onChange={handleYTCheck}
        />
        
        {/* Label text dynamically changes based on the checkbox state */}
        {isChecked ? 'Use Youtube' : 'Use Youtube'}
      </label>
      {visualData && <h2>{visualData}</h2>}
      {isChecke1d && <h2>yes</h2>}
      <h1>{ytLink}</h1>
      <h1>{ytTitle}</h1>
  </div>


  <Button className="coolBlueButton" onClick={handleDetect} 
      style={{position: 'absolute',
        left: 'calc(33.33% + 275px)', // Moves the box to the left third and then 50px to the left
        top: '95%', // Adjust as needed,
        width: '260px',
        transform: 'translateY(-50%)'}}>Detect </Button>

  



  </div>
</div>


    
    </div>
    
  );
}

export default App;