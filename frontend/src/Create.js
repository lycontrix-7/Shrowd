import React, { Component } from 'react';
import './css/auth.css';

export default class Create extends Component {
    constructor(props) {
        super(props);
        this.state = {
            message: '',
            server_type: 's',
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
        if (e.target.id === "s") {
            document.querySelector(".password").style.display = "none";
            e.target.style.display = "none";
            document.querySelector(".privateChange").style.display = "block";
        }
        if (e.target.id === "p") {
            document.querySelector(".password").style.display = "block";
            e.target.style.display = "none";
            document.querySelector(".publicChange").style.display = "block";
        }
            
        this.setState({
            server_type: e.target.id
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
            <div className="auth-form">
                <div className="main">
                    <div className="error">{this.state.message}</div>
                    
                    <div className="name-area">
                        <input className="name" type="text" onChange={this.handleNameChange} />
                        <input className="submit-form" onClick={this.handleSubmit} type="button" value="➤" />
                    </div>
                    
                    <div className="password">
                        <div className="passwordText">Password :</div>
                        <input className="passwordInput" type="text" onChange={this.handlePasswordChange} />             
                    </div>
                    
                    <div onClick={this.handleType} id="p" className="privateChange typeCommon">Create Private Server ?</div>
                    <div onClick={this.handleType} id="s" className="publicChange typeCommon">Create Public Server ?</div>
                </div>
            </div>
        );
    }
}