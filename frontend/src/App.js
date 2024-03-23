import './App.css';
import bg from './cool-background.svg';
import bg2 from './cool-background2.png';
import bg3 from './cool-background3.png';
import gsap from "gsap";
import SplitTextJS from 'split-text-js';
import Button from 'react-bootstrap/Button';




function App() {


  const handleClick = () => {
    alert('Button clicked!');
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
    {/* Content inside the white box */}

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
  <Button className="coolBlueButton" onClick={handleClick} 
      style={{position: 'absolute',
        left: 'calc(33.33% + 275px)', // Moves the box to the left third and then 50px to the left
        top: '95%', // Adjust as needed,
        width: '260px',
        transform: 'translateY(-50%)'}}>Try Demo! </Button>

<div className="checkbox-container" style={{
  position: 'absolute',
  left: '10px'
}}>  
  
</div>



  </div>
</div>


    
    </div>
    
  );
}

export default App;
