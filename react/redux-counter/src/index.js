import React from 'react';
import ReactDOM from 'react-dom';
import App from './containers/App'
import './index.css';
import * as serviceWorker from './serviceWorker';

// 리덕스 관련 불러오기
import { createStore } from 'redux'
import reducers from './reducers'
import { Provider } from 'react-redux'


// 스토어 생성
const store = createStore(reducers, window.devToolsExtension && window.devToolsExtension())

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
