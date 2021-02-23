import React, { Component } from 'react';
import PrivateServer from './PrivateServer';

export default class PrivateValidator extends Component {
    constructor(props) {
        super(props);
        this.state = {
            logged_in: false
        };

        this.name = this.props.match.params.name;
    }

    componentDidMount() {
        var setString = 'AllowedTo_' + this.name
        if (localStorage.getItem(setString)) {
            this.setState({logged_in: true});
        }
    }
    
    render() {
        return(
            <div className="PrivateValidator">
                {this.state.logged_in ? <PrivateServer name={this.name}/> : "Server Dosent exist or you dont have access to it"}             
            </div>
        )
    }
}