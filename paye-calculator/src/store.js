import { createStore } from 'redux';
import { payeReducer } from './reducers/payeReducer';

const store = createStore(payeReducer);

export default store;