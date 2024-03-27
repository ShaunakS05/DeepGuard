import React from 'react';
import { Chart, ArcElement, PieController} from 'chart.js';
import { Doughnut } from 'react-chartjs-2';


Chart.register(ArcElement, PieController);

const PieChartWithText_copy = ({ real, text }) => {
  // Calculate the unfilled portion
  let scoreT = 1;


  
  let color;

  
  
  
    if (real == "real") {
        color = 'green'; // Green for scores greater than 75
    }
    else if(real == "fake") {
      color = 'red'
    }
    else{
      color = 'lightgray'
    }
     
    const unfilled = 1 - scoreT;

  const data = {
    labels: ['Score', 'Remaining'],
    datasets: [
      {
        data: [scoreT, unfilled],
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
        text: `${real}%`, // Dynamic text
        color: "black",
        fontStyle: 'Arial', // Font style
        sidePadding: 5, // Padding
        
      },
    },
  };

  return<div style={{ width: '170px', height: 'px' }}>
    <span style={{position: 'relative', top:'70px', left:'49px', color:'black', textAlign:'center', alignContent:'center', textJustify:'center'}}>{text}</span>
    <span style={{position: 'relative', top:'120px', left:'-15px', color:'black', textAlign:'center', alignContent:'center', textJustify:'center', fontSize:'30px'}}>{real}</span>

  <Doughnut data={data} options={options} />
</div>

};

export default PieChartWithText_copy;
