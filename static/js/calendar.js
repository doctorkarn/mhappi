function setStyle(id,style,value)
{
    id.style[style] = value;
}
function opacity(el,opacity)
{
        setStyle(el,"filter:","alpha(opacity="+opacity+")");
        setStyle(el,"-moz-opacity",opacity/100);
        setStyle(el,"-khtml-opacity",opacity/100);
        setStyle(el,"opacity",opacity/100);
}
function calendar(monthSearch,yearSearch)
{
        monthSearch = monthSearch-1;
        var dateSearch = new Date();
        dateSearch.setMonth(monthSearch);
        dateSearch.setYear(yearSearch);

        var text = "";
        var date = new Date();
        var month = date.getMonth();
        var year = date.getYear() + 1900;
        var dateNow = date.getDate();

        if(yearSearch<=200)
        {
                yearSearch += 1900;
        }
        months = new Array('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December');
        days_in_month = new Array(31,28,31,30,31,30,31,31,30,31,30,31);
        if(yearSearch%4 == 0 && yearSearch!=1900)
        {
                days_in_month[1]=29;
        }
        total = days_in_month[monthSearch];
        var month_today = months[monthSearch];
        var year_today = yearSearch;
        beg_j = dateSearch;
        beg_j.setDate(1);
        if(beg_j.getDate()==2)
        {
                beg_j=setDate(0);
        }
        beg_j = beg_j.getDay();
        text += '<table class="cal_calendar"><tbody id="cal_body"><tr><th class="table-cover" colspan="7"><div class="table-month-left">'+month_today+'</div><div class="table-month-right">'+year_today+'</div></th></tr>';
        text += '<tr class="cal_d_weeks"><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr><tr>';
        week = 0;

        for(i=1;i<=beg_j;i++)
        {
                text += '<td class="cal_days_bef_aft"> </td>';
                week++;
        }
        var dateText = "";
        for(i=1;i<=total;i++)
        {
                if(week==0)
                {
                        text += '<tr>';
                }
                //alert(yearSearch+">="+year+" , "+month+">="+monthSearch+" , "+i+">="+dateNow)
                dateText = yearSearch+'-'+monthSearch+'-'+i;
                if(yearSearch >= year && monthSearch > month){
                    text += '<td id="date_"'+dateText+'" class="cal_day" onclick="setCalendar(\''+dateText+'\',\'\');">'+i+'</td>';
                }
                else if(yearSearch == year && monthSearch == month && i >= dateNow)
                {
                        var check = false;
                        for(var dd = 0; dd < docDay.length; dd++){
                            if(docMonth[dd]-1 == monthSearch) {
                                if(docDay[dd] == i) check = true;
                                if(docDay[dd] > i) break;
                            }
                        }
                        if(check) text += '<td id="date_"'+dateText+'" class="cal_day notify" onclick="setCalendar(\''+dateText+'\',\'\');">'+i+'</td>';
                        else text += '<td id="date_"'+dateText+'" class="cal_day" onclick="setCalendar(\''+dateText+'\',\'\');">'+i+'</td>';
                }
                else{
                    text += '<td> </td>';
                }
                week++;
                if(week==7)
                {
                        text += '</tr>';
                        week=0;
                }
        }
        for(i=1;week!=0;i++)
        {
                text += '<td class="cal_days_bef_aft"> </td>';
                week++;
                if(week==7)
                {
                        text += '</tr>';
                        week=0;
                }
        }
        text += '</tbody></table>';
        document.getElementById('calendar').innerHTML = text;
        return true;
}

var textNow;

function setCalendar(date, time){
    var elem = document.getElementById("clinic_time");
    //alert(date);
    //if(date != "" && time != "") 
        elem.value = date+" "+time;
}