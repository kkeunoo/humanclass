let power = false;
let lastVol = 5;
let muted = true;
const VOL_MAX = 5;
function powerOne() {
    power = !power;
    console.log(power ? '켜짐' : '꺼짐');
}
function volumeUp() {
    if (!power) {
        console.log('전원 꺼짐');
        return;
    }
    muted = false;
    lastVol++;
    if (lastVol > VOL_MAX) {
        lastVol = VOL_MAX;
    }
    console.log(lastVol, muted);
}
volumeUp();
powerOne();
volumeUp();
powerOne();
