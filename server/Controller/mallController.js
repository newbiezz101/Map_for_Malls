const express = require('express');
const router = express.Router();
const Mall = require('../Model/mallSchema');
const mall = "";

router.get("/getMall", async (req, res) => {
    Mall.find({"mallname":mall}, function(err, mall){
        if (err){
            res.send("Something is wrong");
        } else {
            res.send(mall);
            // console.log(req)
        }
    })
    // const posts = await Mall.find()
    // res.send(posts)
    // var mallName = req.param("mallName")
    // res.send(mallName);
});

router.post('/postMall', (req,res,next) => {
    // Mall.findOne({ mallname: req.body.mallName }, (err) => {
    //     if (err) {
    //         return res.status(400).json({ 'msg': err });
    //     }

    //     let mall = new Mall({
    //         mallname: req.body.mallName,
    //     });

    // // Save data in database
    //     mall.save((err, result) => {
    //         if(err) {
    //             console.log(err);
    //         } else {
    //             console.log(result) 
    //         }
    //     });
    // });
    var mall = req.body.mallName;
    res.send(mall);
});


module.exports = router;