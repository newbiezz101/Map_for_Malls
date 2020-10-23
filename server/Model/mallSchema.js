const mongoose = require("mongoose")

const mallSchema = mongoose.Schema({
  mallName: String,
})

module.exports = mongoose.model("malls", mallSchema);