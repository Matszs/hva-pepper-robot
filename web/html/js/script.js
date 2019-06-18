var initMqtt;
var mqttClient;

$(function() {

    $('#say-btn').click(function() {
        var text = $('#say-txt').val();

        mqttClient.publish('pepper/say', text);
    });

    $('#show_1-btn').click(function() {
        mqttClient.publish('pepper/show_1', '');
    });

    $('#show_2-btn').click(function() {
        mqttClient.publish('pepper/show_2', '');
    });

    $('#show_3-btn').click(function() {
        mqttClient.publish('pepper/show_3', '');
    });

    $('#show_4-btn').click(function() {
        mqttClient.publish('pepper/show_4', '');
    });

    $('#wave-btn').click(function() {
        mqttClient.publish('pepper/wave', '');
    });

    $('#bow-btn').click(function() {
        mqttClient.publish('pepper/bow', '');
    });

    $('#dab-btn').click(function() {
        mqttClient.publish('pepper/dab', '');
    });





    initMqtt = function (connectionFunction) {
        if (mqttClient) {
            if (mqttClient.connected) {
                if (typeof (connectionFunction) !== 'undefined')
                    connectionFunction();
            } else {
                mqttClient.on('connected', function () {
                    console.log('MQTT :: Re-init');

                    if (typeof (connectionFunction) !== 'undefined')
                        connectionFunction();
                });
            }
        } else {
            mqttClient = new MQTTClient({
                clientId: 'mqtt-web-' + (Math.floor((Math.random() * 100000) + 1)),
                host: 'mqtt.akoo.nl',
                port: 7778,
                username: 'ldr',
                password: 'xJPriWagGxc68tpwYmDdHWEkg'
            });

            mqttClient.connect();

            mqttClient.on('connected', function () {
                console.log('MQTT :: Connected');

                if (typeof (connectionFunction) !== 'undefined')
                    connectionFunction();
            });

            mqttClient.on('connectionLost', function () {
                setTimeout(function () {
                    console.log('MQTT :: Connection lost');
                    if (mqttClient)
                        mqttClient.connect();

                }, 1000);
            });
        }
    };


    initMqtt(function () {

        mqttClient.on('messageArrived', function (msg) {

        });
    });

});