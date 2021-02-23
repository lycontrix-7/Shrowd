import React from "react";
import Join from "./Join";
import Create from "./Create";
import PublicServer from "./PublicServer";
import PrivateValidator from "./PrivateValidator"
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path='/' component={Join} />
          <Route path='/join' component={Join} />
          <Route path='/create' component={Create} />
          <Route path='/s/:name' component={PublicServer} />
          <Route path='/p/:name' component={PrivateValidator} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
