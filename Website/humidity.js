function myFunction() {
    var selectedDate=document.getElementById("demo1").value;
    console.log(selectedDate);
    const Http = new XMLHttpRequest();
    const url='https://weather-monitoring-12aee-default-rtdb.firebaseio.com/HUMIDITY_data.json';
    Http.onreadystatechange = () => {
        if (Http.readyState == 4 && Http.status == 200) {
            console.log(Http.responseText);
            var resData=JSON.parse(Http.responseText);
            console.log(resData);
            var i;
            var plotData=[];
            for(i=0;i<resData.length;i++){
                var y=resData[i]['reading']
                if(resData[i]['date']==selectedDate){
                    var humid1=resData[i]['date'].split('-');
                    var humid2=resData[i]['time'].split(':');
                    var x=new Date(humid1[0],humid1[1]-1,humid1[2],humid2[0],humid2[1]);
                    console.log(x,y);
                    plotData.push({x:x,y:y});
                } 
            }
            //console.log(plotData);
            if(plotData.length!=0){
                var chart = new CanvasJS.Chart("chartContainer",
                {
                    title:{text: "Humidity Data"},
                    axisX:{gridColor: "lightgreen" ,gridThickness: 2},
                    axisY:{gridColor: "lightgreen"},
                    data: [{type: "line",dataPoints: plotData}]
                });
                chart.render();
            }
            else{
                document.getElementById("chartContainer").innerHTML="No data available for this date."
            }
        }
    }
    Http.open("GET", url);
    Http.send();
}