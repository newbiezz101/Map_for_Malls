const express = require('express');
const router = express.Router();
const Mall = require('../Model/mallSchema');

router.get("/mall", async (req, res) => {
    const posts = await Mall.find()
    res.send(posts)
});


module.exports = router;