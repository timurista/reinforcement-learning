const { chromium } = require('playwright');
const { saveVideo } = require('playwright-video');
const { getAction } = require('./action_policy')

function delay(t, val) {
    return new Promise(function(resolve) {
        setTimeout(function() {
            resolve(val);
        }, t);
    });
 }

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();
  const ts = new Date().getTime();
  
  // mario example for testing
  // https://supermarioplay.com/fullscreen
  await page.goto('https://supermarioplay.com/fullscreen');
  await page.click('body')
  const capture = await saveVideo(page, `/tmp/video_mario_${ts}.mp4`);
  await delay(1000);
  
  for (let i=0; i<100;i++ ) {
    // await page.keyboard.press('ArrowRight');
    let action = getAction();
    console.log("action",action)
    await page.keyboard.down(action);
    await delay(200);
    await page.keyboard.up(action);

    // takes a bit for action to finish
    await delay(500);
  }

  capture.stop();
  await browser.close();
})();
