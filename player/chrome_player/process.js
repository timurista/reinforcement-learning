// const ffmpegdotjs = require("ffmpegdotjs");
var ffmpeg = require('fluent-ffmpeg');
ffmpeg.setFfmpegPath("node_modules/@ffmpeg-installer/darwin-x64/ffmpeg")
var command = ffmpeg();
var fs = require('fs')


videoPath="/tmp/video_mario_1614183995850.mp4"
outPath="/tmp/video_mario_1614183995850_edited.mp4"
// ffmpegdotjs.trimvideo(videoPath,0,15,outPath).then((file)=>{
//         console.log(file);
// });

var out  = fs.createWriteStream(outPath);


ffmpeg(videoPath).size('640x360').duration('0:15').on('error', function(err) {
  console.log('An error occurred: ' + err.message);
}).on('end', function() {
  console.log('Processing finished !');
}).writeToStream(out, { end: true });
