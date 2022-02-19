function App() {
    
    const [count, setCount] = React.useState(0)


    return (
      <React.Fragment>
        <span>{count}</span>
        <br />
        <button onClick={() => setCount(count + 1)}>
          Increment
        </button>
      </React.Fragment>
      
    );
  }

ReactDOM.render(<App/>, document.querySelector("#root"))