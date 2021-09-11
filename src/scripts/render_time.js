dayjs.extend(window.dayjs_plugin_utc)

document$.subscribe(function() {
    var timezone = document.getElementById("timezone")
    if (!!timezone) {
        timezone.innerText = Intl.DateTimeFormat().resolvedOptions().timeZone
    };
    for (let time of document.getElementsByTagName("time")) {
        time.innerText = dayjs(time.dateTime).local().format("MMMM D H:mm");
    }
});
