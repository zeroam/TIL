import React, { useRef } from 'react'

const ScrollBox = () => {
    const box = useRef();

    const style = {
        border: '1px solid black',
        height: '300px',
        width: '300px',
        overflow: 'auto',
        position: 'relative'
    }

    const innerStyle = {
        width: '100%',
        height: '650px',
        background: 'linear-gradient(white, black)'
    }

    const scrollToBottom = () => {
        const { scrollHeight, clientHeight } = box.current
        box.current.scrollTop = scrollHeight - clientHeight
    }

    return (
        <>
            <div
                style={style}
                ref={box}>
                <div style={innerStyle} />
            </div>
            <button onClick={scrollToBottom}>
                맨 밑으로
            </button>
        </>
    )
}

export default ScrollBox