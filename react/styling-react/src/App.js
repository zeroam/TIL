import React from 'react';
import classNames from 'classnames/bind'
import Button from './components/Button'
import StyledButton from './StyledButton'
import styles from './App.module.scss'

const cx = classNames.bind(styles)

function App() {
  const isBlue = true;

  return (
    <>
      <div className={cx('box', {
        blue: isBlue
      })}>
        <div className={cx('box-inside')}/>
      </div>
      <Button>버튼</Button>
      <StyledButton>버튼 </StyledButton>
      <StyledButton big>버튼 </StyledButton>
    </>
  );
}

export default App;
