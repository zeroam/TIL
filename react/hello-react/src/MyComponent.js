import React, { useState } from "react";
import PropTypes from "prop-types";


function MyComponent(props) {
    const [number, setNumber] = useState(0);

    function increment() {
        setNumber(prevState => prevState + 1);
    }

    return (
        <>
            <div>새로운 컴포넌트</div>
            <div>제 이름은 {props.name} 입니다.</div>
            <div>저는 {props.age}살 입니다.</div>
            <p>숫자: {number}</p>
            <button onClick={increment}>더하기</button>
        </>
    )
}

MyComponent.defaultProps = {
    name: "기본이름"
}

MyComponent.propTypes = {
    name: PropTypes.string,  // name props 타입을 문자열로 설정합니다.
    age: PropTypes.number.isRequired,  // 필수적으로 존재해야 하며, 숫자입니다.
}

export default MyComponent;
