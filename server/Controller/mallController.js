const express = require('express');
const router = express.Router();
const User = require('../Model/mallSchema');

// router.get('/mall', (req,res) => {
    
//     console.log("Succesfully connected to Navigation API");
//     // res.send("API is here");
    
// });

router.get("/users", async (req, res) => {
    const posts = await User.find()
    res.send(posts)
});


module.exports = router;