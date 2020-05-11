import React, { Fragment } from 'react';
import MyComponent from "./MyComponent";
import "./App.css";


function App() {
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

  return (
    <Fragment>
      <div className="my-div">
        <h1>리액트</h1>
        <h2>{text}</h2>
        {condition && "보여주세요"}
        <div style={style}></div>
      </div>
      <MyComponent name="React" age={32} />
      <MyComponent age={23} />
    </Fragment>
  )
}

export default App;
