import React from 'react';
import { Chart, ArcElement, PieController} from 'chart.js';
import { Doughnut } from 'react-chartjs-2';


Chart.register(ArcElement, PieController);

const PieChartWithText = ({ score, text }) => {
  // Calculate the unfilled portion
  const unfilled = 1 - score;


  
  let color;

  if(text == "Visual Data")
  {
        if(score == "real")
        {
            score = 1;
        }
        else
        {
            score = 0;
        }
  }
  else
  {
    if (score > 0.75) {
      color = 'green'; // Green for scores greater than 75
    } else if (score > .30) {
      color = 'orange'; // Orange for scores between 31 and 75
    } else {
      color = 'red'; // Red for scores 30 or below
    }
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
        color: "black",
        fontStyle: 'Arial', // Font style
        sidePadding: 5, // Padding
        
      },
    },
  };
  
  return<div style={{ width: '170px', height: 'px' }}>
    <span style={{position: 'relative', top:'70px', left:'49px', color:'black', textAlign:'center'}}>{text}</span>
    <span style={{position: 'relative', top:'120px', left:'-17px', color:'black', textAlign:'center', fontSize:'30px'}}>{score}</span>

  <Doughnut data={data} options={options} />
</div>

};

export default PieChartWithText;
