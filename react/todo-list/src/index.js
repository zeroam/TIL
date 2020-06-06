import React from 'react';
import ReactDOM from 'react-dom';
import './styles/main.module.scss';
import App from './components/App';
import * as serviceWorker from './serviceWorker';

import modules from './modules'
import { createStore } from 'redux'
import { Provider } from 'react-redux'

const store = createStore(modules, window.devToolsExtension && window.devToolsExtension())

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
