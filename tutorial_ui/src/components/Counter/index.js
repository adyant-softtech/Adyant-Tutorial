
import {useSelector, useDispatch} from 'react-redux'

const Counter = () =>{
    
    const counter = useSelector(state => state.counter);
    const dispatch = useDispatch()

    const incrementHandler = () =>{
        dispatch({type : 'increment'})
    }

    const decrementHandler = () =>{
        dispatch({type : 'decrement'})
    }

    return(
        <div>
            <h1>
                Redux Counter
            </h1>
            <div>
                <span>{counter}</span>
            </div>
            <div>
                <button onClick={incrementHandler}>Increement</button>
                <button onClick={decrementHandler}>Decrement</button>
            </div>
        </div>
    )
}

export default Counter;