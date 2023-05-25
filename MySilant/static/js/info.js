if (!localStorage.getItem('pageLoaded')) {
    if (typeof location.search.split('order_by=')[1] == "undefined") {
        reload();
    }
}
function setOrder_by(name) {
    window.sessionStorage.setItem('order_by', name);
    reload();
}
function setFilter_te(name) {
    window.sessionStorage.setItem('te', "&te=" + name);
    reload();
}
function setFilter_en(name) {
    window.sessionStorage.setItem('en', "&en=" + name);
    reload();
}
function setFilter_tr(name) {
    window.sessionStorage.setItem('tr', "&tr=" + name);
    reload();
}
function setFilter_da(name) {
    window.sessionStorage.setItem('da', "&da=" + name);
    reload();
}
function setFilter_sa(name) {
    window.sessionStorage.setItem('sa', "&sa=" + name);
    reload();
}
function reset() {
    sessionStorage.clear();
    reload();
}

function reload() {
    if (window.sessionStorage.getItem('order_by') === null) {order_by = "?order_by=date_of_shipment_from_the_factory";}
    else{order_by = window.sessionStorage.getItem('order_by');}
    if (window.sessionStorage.getItem('te') === null) {te = "";}else{te = window.sessionStorage.getItem('te');}
    if (window.sessionStorage.getItem('en') === null) {en = "";}else{en = window.sessionStorage.getItem('en');}
    if (window.sessionStorage.getItem('tr') === null) {tr = "";}else{tr = window.sessionStorage.getItem('tr');}
    if (window.sessionStorage.getItem('da') === null) {da = "";}else{da = window.sessionStorage.getItem('da');}
    if (window.sessionStorage.getItem('sa') === null) {sa = "";}else{sa = window.sessionStorage.getItem('sa');}
    httpParam = order_by + te + en + tr + da + sa;
    window.location.href = httpParam;

}
