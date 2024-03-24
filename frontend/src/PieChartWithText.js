import React from 'react';
import { Chart, ArcElement, PieController} from 'chart.js';
import { Doughnut } from 'react-chartjs-2';


Chart.register(ArcElement, PieController);

const PieChartWithText = ({ score, text }) => {
  // Calculate the unfilled portion
  const unfilled = 100 - score;

  let color;
  if (score > 75) {
    color = 'green'; // Green for scores greater than 75
  } else if (score > 30) {
    color = 'orange'; // Orange for scores between 31 and 75
  } else {
    color = 'red'; // Red for scores 30 or below
  }
  const data = {
    labels: ['Score', 'Remaining'],
    datasets: [
      {
        data: [score, unfilled],
        backgroundColor: [color, 'lightgrey'],
        hoverBackgroundColor: [color, 'lightgrey'],
        borderWidth: 0,
      },
    ],
  };

  const options = {
    cutout: '70%', // Adjust this value to make the doughnut thinner or thicker
    plugins: {
      tooltip: {
        enabled: false, // Disable tooltip
      },
      legend: {
        display: false, // Hide legend
      },
    },
    elements: {
      center: {
        text: `${score}%`, // Dynamic text
        color: '#FF6384', // Text color
        fontStyle: 'Arial', // Font style
        sidePadding: 5, // Padding
        
      },
    },
  };

  return<div style={{ width: '150px', height: '150px' }}>
    <span style={{position: 'relative', top:'50px', left:'36px', color:'white', textAlign:'center'}}>{text}</span>
    <span style={{position: 'relative', top:'70px', left:'14px', color:'white', textAlign:'center'}}>{score}</span>

  <Doughnut data={data} options={options} />
</div>

};

export default PieChartWithText;
