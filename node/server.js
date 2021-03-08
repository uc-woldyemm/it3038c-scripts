var fs = require("fs");
var http = require("http"); 
var os = require("os");
var ip = require("ip");
var day = os.uptime/86400;
var hour =  (day) / 24 * 10;
var minute = (hour) / 60 * 10;
var second = (minute) / 60 * 10;

var days = day.toFixed(2)
var hours = hour.toFixed(2)
var minutes = minute.toFixed(2)
var seconds = second.toFixed(2)

var server = http.createServer(function(req, res) {
    if (req.url === "/" ) {
        fs.readFile("node/public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    }

    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`
        <!DOCTYPE html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${days} ${hours} ${minutes} ${seconds}</p>
            <p>Total Memory: ${os.totalmem/800000}MB</p>
            <p>Free Memory: ${os.freemem/800000}MB</p>
            <p>Number of CPUs: ${cpuData = os.cpus}</p>
        </body>
        </html>
        `
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);
    }

    else {
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }

});

server.listen(3000);
console.log("Server listening on port 3000");
