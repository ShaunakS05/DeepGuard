import React from 'react';
import './Button.css'; // Import the CSS file for styling

const BlueButton = ({ text, onClick }) => {
  return (
    <button className="coolBlueButton" onClick={onClick}>
      {text}
    </button>
  );
};

export default BlueButton;
