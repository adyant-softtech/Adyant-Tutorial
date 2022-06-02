import './App.css';
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom';
import 'antd/dist/antd.css';
import Login from './components/LoginForm';
import Counter from './components/Counter';

function App() {
  return (
    <div>
      <Router>
        {/* <div>
          <MainHeader />
        </div> */}
        <Routes>
              <Route exact path='/' element={< Login />}></Route>
              {/* <Route exact path='/' element={< Counter />}></Route> */}
        </Routes>
        {/* <div>
          <Footer />
        </div> */}
      </Router>
    </div>
    );
}

export default App;
