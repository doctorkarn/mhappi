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
        var countWeek = 0;

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
                dateText = yearSearch+'-'+monthSearch+'-'+i;
                if((yearSearch == year && monthSearch > month) || (yearSearch == year && monthSearch == month && i >= dateNow) || (yearSearch > year))
                {
                        var check = false;
                        var index = -1;
                        var allDay = false;
                        for(var dd = 0; dd < docDay.length; dd++){
                            if(docMonth[dd]-1 == monthSearch) {
                                if(index > -1 && docDay[dd] == docDay[index]) { allDay = true; }
                                if(docDay[dd] == i) { check = true; index = dd; }
                            }
                        }

                        if(check && yearSearch == year && patientAppoint) {
                            if(allDay) text += '<td id="date_'+dateText+'_all" class="cal-day-all" onclick="setCalendarDateId(\''+dateText+'\',\'all\',[\''+docId[index-1]+'\',\''+docId[index]+'\']);"><div class="day-selected-choose"><div class="day-selected-left"></div><div class="day-selected-right"></div><div class="day-selected-text">'+i+'</div></div></div>';
                            else if(docHour[index] < 13) text += '<td id="date_'+dateText+'_m" class="cal-day-morning" onclick="setCalendarDateId(\''+dateText+'\',\'m\',[\''+docId[index]+'\']);"><div class="day-selected-choose"><div class="day-selected-left"></div><div class="day-selected-right" style="opacity:0"></div><div class="day-selected-text">'+i+'</div></div></div>';
                            else text += '<td id="date_'+dateText+'_a" class="cal-day-afternoon" onclick="setCalendarDateId(\''+dateText+'\',\'a\',[\''+docId[index]+'\']);"><div class="day-selected-choose"><div class="day-selected-left" style="opacity:0"></div><div class="day-selected-right"></div><div class="day-selected-text">'+i+'</div></div></div>';
                        }
                        else if(check && yearSearch == year) {
                            if(allDay) text += '<td id="date_'+dateText+'_all" class="cal-day-all" onclick="setCalendarDate(\''+dateText+'\',\'all\');"><div class="day-selected-choose"><div class="day-selected-left"></div><div class="day-selected-right"></div><div class="day-selected-text">'+i+'</div></div></div>';
                            else if(docHour[index] < 13) text += '<td id="date_'+dateText+'_m" class="cal-day-morning" onclick="setCalendarDate(\''+dateText+'\',\'m\');"><div class="day-selected-choose"><div class="day-selected-left"></div><div class="day-selected-right" style="opacity:0"></div><div class="day-selected-text">'+i+'</div></div></div>';
                            else text += '<td id="date_'+dateText+'_a" class="cal-day-afternoon" onclick="setCalendarDate(\''+dateText+'\',\'a\');"><div class="day-selected-choose"><div class="day-selected-left" style="opacity:0"></div><div class="day-selected-right"></div><div class="day-selected-text">'+i+'</div></div></div>';
                        }
                        else text += '<td id="date_'+dateText+'_none" class="cal-day">'+i+'</td>';
                }
                else{
                    text += '<td class="cal_days_bef_aft"> </td>';
                }
                week++;
                if(week==7)
                {
                        text += '</tr>';
                        week=0;
                        countWeek++;
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
                        countWeek++;
                }
        }
        if(countWeek < 6){
            countWeek++;
            text += '<tr>';
            for(i=1;i<=7;i++)
            {
                text += '<td class="cal_days_bef_aft"> </td>';
                week++;
                if(week==7)
                {
                        text += '</tr>';
                        week=0;
                        countWeek++;
                }
            }
        }
        text += '</tbody></table>';
        document.getElementById('calendar').innerHTML = text;
        return true;
}

var notifyType = ""; 
var textDateNow = "";
var notifyNow = "";
var textTimeNow = "";
var textClinicId;

function setCalendarDate(date,notify){

    resetForm();

    var day = date.split('-')[2];
    var lastDay = textDateNow.split('-')[2];

    if(textDateNow == date) {
        if(document.getElementById("date_"+textDateNow+"_"+notifyNow) !== null){
            if(notifyNow == "m") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-morning";
            else if(notifyNow == "a") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-afternoon";
            else if(notifyNow == "all") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-all";
        }
        textDateNow = "";
    }
    else {

        if(document.getElementById("date_"+textDateNow+"_"+notifyNow) !== null){
            if(notifyNow == "m") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-morning";
            else if(notifyNow == "a") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-afternoon";
            else if(notifyNow == "all") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-all";
        }

        textDateNow = date;
        notifyNow = notify;

        if(notifyNow == "m") {
            document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-morning-select";
            showCancelMorning();
            cancelMorning();
        }
        else if(notifyNow == "a") {
            document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-afternoon-select";
            showCancelAfternoon();
            cancelAfternoon();
        }
        else if(notifyNow == "all") {
            document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-all-select";
            showCancelMorning();
            showCancelAfternoon();
            cancelMorning();
            cancelAfternoon();
        }
    }
    textTimeNow = "";
}

function setCalendarDateId(date,notify,id){

    resetAppointForm();

    var day = date.split('-')[2];
    var lastDay = textDateNow.split('-')[2];

    if(textDateNow == date) {
        if(document.getElementById("date_"+textDateNow+"_"+notifyNow) !== null){
            if(notifyNow == "m") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-morning";
            else if(notifyNow == "a") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-afternoon";
            else if(notifyNow == "all") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-all";
        }
        textDateNow = "";
        textClinicId = "";
    }
    else {

        if(document.getElementById("date_"+textDateNow+"_"+notifyNow) !== null){
            if(notifyNow == "m") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-morning";
            else if(notifyNow == "a") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-afternoon";
            else if(notifyNow == "all") document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-all";
        }

        textDateNow = date;
        notifyNow = notify;
        textClinicId = id;

        if(patientAppoint){
            if(notifyNow == "m") setAppointClinicTimeM(textClinicId[0]);
            else if(notifyNow == "a") setAppointClinicTimeA(textClinicId[0]);
            else if(notifyNow == "all") {
                setAppointClinicTimeM(textClinicId[0]);
                setAppointClinicTimeA(textClinicId[1]);
            }
        }

        if(notifyNow == "m") {
            document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-morning-select";
            showCancelMorning();
        }
        else if(notifyNow == "a") {
            document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-afternoon-select";
            showCancelAfternoon();
        }
        else if(notifyNow == "all") {
            document.getElementById("date_"+textDateNow+"_"+notifyNow).className = "cal-day-all-select";
            showCancelMorning();
            showCancelAfternoon();
        }
    }

}

var currentDate = new Date();
var currentMonth = currentDate.getMonth() + 1;
var currentYear = currentDate.getYear() + 1900;

var monthCount = currentMonth;
var yearCount = currentYear;

function nextMonth(){

    document.getElementById("left-button").className = "left-button";
    monthCount++;
    if(monthCount > 12){
        monthCount = 1;
        yearCount++;
    }

    resetForm();
    calendar(monthCount,yearCount);
}

function backMonth(){
    if((yearCount == currentYear && monthCount > currentMonth) || (yearCount > currentYear)){
        monthCount--;
        if(monthCount < 1){
            monthCount = 12;
            yearCount--;
        }

        if(monthCount <= currentMonth && yearCount <= currentYear){
            document.getElementById("left-button").className = "left-button-disable";
            monthCount = currentMonth;
            yearCount = currentYear;
            calendar(monthCount,yearCount);
            resetForm();
        }
        else {
            calendar(monthCount,yearCount);    
            resetForm();
        }
    }
}

function cancelMorning(){
    var elem = document.getElementById("clinic_time_m");
    elem.value = textDateNow + " 9:00";
}

function cancelAfternoon(){
    var elem = document.getElementById("clinic_time_a");
    elem.value = textDateNow + " 13:00";
}

function clearField(){
    var elem_m = document.getElementById("clinic_time_m");
    elem_m.value = "";
    var elem_a = document.getElementById("clinic_time_a");
    elem_a.value = "";
}

function resetForm(){
    hideCancelMorning();
    hideCancelAfternoon();
    clearField();           
}

function resetAppointForm(){
    hideCancelMorning();
    hideCancelAfternoon();
    var elem_m = document.getElementById("clinic_time_m");
    elem_m.value = "";
    var elem_a = document.getElementById("clinic_time_a");
    elem_a.value = "";
}

function setAppointClinicTimeM(id){    
    var elem = document.getElementById("clinic_time_m");
    elem.value = id;
}

function setAppointClinicTimeA(id){    
    var elem = document.getElementById("clinic_time_a");
    elem.value = id;
}

function showCancelMorning(){
    document.getElementById("cancel-m").className = "cancel-button";
    document.getElementById("cancel-m").disabled = false;
}

function hideCancelMorning(){
    document.getElementById("cancel-m").className = "cancel-button-disable";
    document.getElementById("cancel-m").disabled = true;
}

function showCancelAfternoon(){
    document.getElementById("cancel-a").className = "cancel-button";
    document.getElementById("cancel-a").disabled = false;
}

function hideCancelAfternoon(){
    document.getElementById("cancel-a").className = "cancel-button-disable";
    document.getElementById("cancel-a").disabled = true;
}

var patientAppoint = false;

function setPatientAppoint(check){
    patientAppoint = check;
}
