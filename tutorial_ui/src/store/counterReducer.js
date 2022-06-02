const counterState = {
    counter: 0
}

const counterReducer = (state = counterState, action) => {
    if (action.type === 'increment'){
        return {
            counter: state.counter + 1
        }
    }

    if (action.type === 'decrement'){
        return {
            counter: state.counter - 1
        }
    }
    return state
}

export default counterReducer;