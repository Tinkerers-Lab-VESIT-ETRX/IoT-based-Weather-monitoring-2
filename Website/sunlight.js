function myFunction() {
    var selectedDate=document.getElementById("demo3").value;
    console.log(selectedDate);
    const Http = new XMLHttpRequest();
    const url='https://weather-monitoring-12aee-default-rtdb.firebaseio.com/LIGHT_INTENSITY_data.json';
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
                    var ldr1=resData[i]['date'].split('-');
                    var ldr2=resData[i]['time'].split(':');
                    var x=new Date(ldr1[0],ldr1[1]-1,ldr1[2],ldr2[0],ldr2[1]);
                    console.log(x,y);
                    plotData.push({x:x,y:y});
                } 
            }
            //console.log(plotData);
            if(plotData.length!=0){
                var chart = new CanvasJS.Chart("chartContainer",
                {
                    title:{text: "Sunlight Intensity Data"},
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