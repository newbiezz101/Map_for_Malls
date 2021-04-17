import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { MallService } from '../services/mall.service';


@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})


export class HomePage implements OnInit {
  // private icons = [
  //   'KLCC'
  // ];
 
  // public items: Array<{ title: string; icon: string }> = [];
  // public allItems: Array<{ title: string; icon: string }> = [];

  // constructor(private router: Router) {
    // for (let i = 0; i < this.icons.length; i++) {
    //   this.items.push({
    //     title: this.icons[i].charAt(0).toUpperCase() + this.icons[i].slice(1),
    //     icon: this.icons[i]
    //   });
    // }
    // this.allItems = this.items;
  // }

  // onSearchTerm(ev: CustomEvent) {
  //   this.items = this.allItems;
  //   const val = ev.detail.value;
  //   var elem = document.getElementById("content");
    
  //   elem.classList.remove("hide");

  //   if (val && val.trim() !== '') {
  //     this.items = this.items.filter(term => {
  //       return term.title.toLowerCase().indexOf(val.trim().toLowerCase()) > -1;
  //     })
  //   }

  //   //console.log(this.allItems[0]);
  //   //if (this.items == [{title: "KLCC", icon: "KLCC"}]){alert("KLCC")}
  // }

  //call this function when bg is click, add hide to content
  // clickChange(ev : CustomEvent) {
  //   var elem = document.getElementById("content");
  //   elem.classList.add("hide");
  // }

  // click_item(item: object){
  //   console.log(item);
  //   alert(this.items);  
  // }

  // navigate(){
  //   this.router.navigate(['/shop_search'])
  // }
  mallForm: FormGroup;
  mall: any;

  constructor(private formBuilder: FormBuilder, private mallService: MallService,private router: Router) {}

  ngOnInit(){
    this.mallForm = this.formBuilder.group({
      mallName: ['', [Validators.required]]
    });
  }

  getMallService(){
    this.mallService.getMall().subscribe(
      response => {
        this.mall = response;
        for (var index in this.mall) {
          // console.log(index);
          if (this.mall[index].mallname.toUpperCase( ) == this.mallForm.value.mallName.toUpperCase( )) {
            // console.log("This is " + this.mallForm.value.mallName);
            console.log(this.mall[index]);
            this.router.navigateByUrl('/shop-search');
            return this.mall[index];
          }
        }   
        // this.router.navigateByUrl('/shop-search');
      },
      err => {
        console.log(err);
      },
      () => {
        console.log('done loading api');
      }
      
    );
  }

  // postMallService(){
    
  //     // console.log(this.mallForm.value);
  //     this.mallService.postMall(this.mallForm.value).subscribe(data => {
  //       console.log(data);
  //     },
  //     err => {
  //       console.log(err);
  //     },
  //     () => {
  //       console.log('done loading api');
  //     }
      
  //     );
  //     this.router.navigateByUrl('/shop-search');
      
  // }
  
}
