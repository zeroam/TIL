import React, { Fragment, useState } from 'react';
import MyComponent from "./MyComponent";
import ValidationSample from './ValidationSample'
import ScrollBox from './ScrollBox'
import IterationSample from './IterationSample'
import "./App.css";
import LifeCycleSample from './LifeCycleSample';


// 랜덤 색상을 생성합니다.
function getRandomColor() {
  return '#' + Math.floor(Math.random() * 16777215).toString(16)
}

function App() {
  const [color, setColor] = useState('#000000')

  const text = "안녕하세요?"
  const condition = true;
  const style = {
    backgroundColor: "gray",
    border: "1px solid black",
    height: Math.round(Math.random() * 300) + 50,
    width: Math.round(Math.random() * 300) + 50,
    WebkitTransition: "all",
    MozTransition: "all",
    msTransition: "all",
  }

  const handleClick = () => {
    setColor(getRandomColor())
  }

  return (
    <Fragment>
      <div>
        <button onClick={handleClick}>랜덤 색상</button>
        <LifeCycleSample color={color} />
      </div>
      <IterationSample />
      <ScrollBox />
      <div className="my-div">
        <h1>리액트</h1>
        <h2>{text}</h2>
        {condition && "보여주세요"}
        <div style={style}></div>
      </div>
      <MyComponent name="React" age={32} />
      <MyComponent age={23} />

      <ValidationSample />
    </Fragment>
  )
}

export default App;
