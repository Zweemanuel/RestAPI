const https = require('https')
const fs = require('fs')

const UrL = 'https://www.metaweather.com/api/location/608105/'
/* const UrL = "https://www.google.com" */
https.get(UrL, (res)=> {
    res.setEncoding('utf8')
    let body=''
    res.on('data', (data) => {
        body += data
    })
    res.on('end', () => {
        body=JSON.parse(body)
        console.log(`City: ${body.title}; Weather State: ${body.consolidated_weather[0].weather_state_name}.`,
                    )
    })
    res.on('end', () => {
        fs.writeFile('data.json', body.toString(), 'utf8', (err)=> {
            if (err) return err
            console.log('Segmentation Fault')
            return 1
        })
    })
})
