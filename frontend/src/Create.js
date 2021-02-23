import React, { Component } from 'react';

export default class Create extends Component {
    constructor(props) {
        super(props);
        this.state = {
            message: '',
            server_type: '',
            name: '',
            password: '',
        }

        this.handleNameChange = this.handleNameChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleType = this.handleType.bind(this);
    }

    handleNameChange (e) {
        this.setState({
            name: e.target.value
        });
    }

    handlePasswordChange (e) {
        this.setState({
            password: e.target.value
        });
    }

    handleType (e) {
        this.setState({
            server_type: e.target.value
        });
    }

    handleSubmit () {
        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type' : 'application/json'},
            body: JSON.stringify({
                name: this.state.name,
                password: this.state.password
            }),
        };
        fetch('http://127.0.0.1:8000/api/' + this.state.server_type + '/create/', requestOptions)
            .then((response) => {
                if (response.ok) {
                    var setString = 'AllowedTo_' + this.state.name
                    localStorage.setItem(setString, true);
                    this.props.history.push("/" + this.state.server_type + "/" + this.state.name)
                }
                else {
                    this.setState({message: response.statusText})
                }
            })
            // Alt way:
            // (data.name[0] === "server with this name already exists.") ? 
            // (this.setState({message: data.name})) : (this.props.history.push("/s/" + data.name))   
        }

    render() {
        return(
            <div className="Create">
                {this.state.message}
                Name:
                <input type="text" onChange={this.handleNameChange}/><br/>
                Password:
                <input type="text" onChange={this.handlePasswordChange}/><br/><br/>             
                
                Server Type:<br/>
                <input type="radio" id="public-server" name="server-type" value="s" onChange={this.handleType}/>
                <label htmlFor="public-server">Public</label><br/>
                <input type="radio" id="private-server" name="server-type" value="p" onChange={this.handleType}/>
                <label htmlFor="private-server">Private</label><br/><br/>

                <button onClick={this.handleSubmit}>Create</button>
            </div>
        );
    }
}