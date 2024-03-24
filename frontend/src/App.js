import './App.css';
import bg from './cool-background.svg';
import bg2 from './cool-background2.png';
import bg3 from './cool-background3.png';
import gsap from "gsap";
import {React, useState} from 'react';
import FileForm from './Componets/FileForm';
import SplitTextJS from 'split-text-js';
import Button from 'react-bootstrap/Button';




function App() {

  const endpoint_Visual = "http://localhost:8000/check-visual-deepfake"
  const endpoint_Audio = "http://localhost:8000/check-audio-deepfake"
  const endpoint_Text = "http://localhost:3000/check-text-deepfake" 

  const[vis, setVis] = useState(null);
  const[file, setFile] = useState(null);

  const[useVisual, setVisual] = useState(false);
  const[useAudio, setAudio] = useState(false);
  const[useText, setText] = useState(false);

  const[visualData, setVisData] = useState(null);
  const[audioData, setAudData] = useState(null);
  const[textData, setTexData] = useState(null);

  const[ytLink, setYTlink] = useState(null);
  const[useYoutube, setYoutubeCheck] = useState(null);


  const [isChecke1d, setIsChecke1d] = useState(false);

  const [isChecked, setIsChecked] = useState(false);



  const handleFile = (event) => {
    setFile(event.target.files[0])
  }
  const handleDetect = async (event) => {
    setIsChecke1d(true);
    event.preventDefault();

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
 
  const handleClick = () => {
    alert('Button clicked!');
  };

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
    <div>
            <h1>Upload File</h1>
            <form style={{alignContent:'center'}}>
                <input type="file" onChange={handleFile}></input>
                        
            </form>
            {file && <p>{file.name}</p>}
        </div>

    <textarea
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
 }} placeholder="Name of person..." />

 
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
