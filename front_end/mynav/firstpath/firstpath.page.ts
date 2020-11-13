import { Component, ViewChild, ElementRef, OnInit } from '@angular/core';

let points = 1;

var path = [[1,2],[3,4],[5,6],[7,8],[10,10],[20,20],[30,30],[40,100]];
var nav_path = '{"1": "function() {return [3,4];}","2": "function() {return [5,6];}","3": "function() {return [8,8];}","4": "function() {return [4,9];}","5": "function() {return [20,20];}","6": "function() {return [30,40];}","7": "function() {return [61,61];}"}';
let x = 0;
var new_path = {"path": "{(1,2),(3,4),(5,6),(40,100)}"}


@Component({
  selector: 'app-firstpath',
  templateUrl: './firstpath.page.html',
  styleUrls: ['./firstpath.page.scss'],
})
export class FirstpathPage implements OnInit{
  @ViewChild('canvas', { static:true })

  canvas : ElementRef<HTMLCanvasElement>;

  private context: CanvasRenderingContext2D;
  
  constructor() {  
  }
  ngOnInit(): void {
    this.context = this.canvas.nativeElement.getContext('2d');
  }
  
  animate() {
    const userStr = JSON.stringify(new_path);
    JSON.parse(userStr, (key, value) => {
      if (typeof value === 'string') {
        return value.toUpperCase();
      }
      return value;
    });
    const check = JSON.parse(nav_path);
  //var map_path = eval("(" + check[2] + ")"); try git test
    //console.log(map_path()[0]);
    var y=3;
    var z: number;
    for(x=1;x<20;x++){
    var map_path = eval("(" + check[x] + ")");
    // console.log("This is map path" + map_path);
    function path() { return map_path};
    console.log("This is map path" + path());
    this.context.fillStyle = 'red';  
    this.context.fillRect(map_path()[0],map_path()[1], 5, 5);
    //console.log(nav_path);
      
    }
  }

}