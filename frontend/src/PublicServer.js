import React, { Component } from 'react';
import './css/server.css'

export default class PublicServer extends Component {
    constructor(props) {
        super(props);
        this.state = {
        };

        this.name = this.props.match.params.name;
    }

    componentDidMount () {
        document.querySelector(".message-input").focus();
        
        const chatSocket = new WebSocket(
            'ws://127.0.0.1:8000/ws/s_'
            + this.name
            + '/'
        );

        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            console.log(e);
            document.querySelector('.message-log').innerHTML += (
                    '<div class="message">' + data.message + '<div>'
                );
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

        document.querySelector('.message-input').onkeyup = function(e) {
            if (e.keyCode === 13) {
                document.querySelector('.message-submit').click();
            }
        };

        document.querySelector('.message-submit').onclick = function(e) {
            const messageInputDom = document.querySelector('.message-input');
            const message = messageInputDom.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInputDom.value = '';
        };
    }

    render() {
        return (
            <div className="server">
                <div className="message-log">
                    
                </div>
                <div className="submit">
                    <input className="message-input" type="text" placeholder="Type message here ..."/>
                    <input className="message-submit" type="button" value="➤" />
                </div>
            </div>
        );
    }
}

