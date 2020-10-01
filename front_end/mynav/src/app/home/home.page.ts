import { Component } from '@angular/core';
import { element } from 'protractor';
import { createPublicKey } from 'crypto';
import { title } from 'process';
import { ShopSearchPage } from 'C:/Users/Acer/Desktop/nav/mynav/shop-search/shop-search.page';
import { Router } from '@angular/router';


@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})


export class HomePage {
  private icons = [
    'KLCC'
  ];
 
  public items: Array<{ title: string; icon: string }> = [];
  public allItems: Array<{ title: string; icon: string }> = [];

  constructor(private router: Router) {
    for (let i = 0; i < this.icons.length; i++) {
      this.items.push({
        title: this.icons[i].charAt(0).toUpperCase() + this.icons[i].slice(1),
        icon: this.icons[i]
      });
    }
    this.allItems = this.items;

  }

  onSearchTerm(ev: CustomEvent) {
    this.items = this.allItems;
    const val = ev.detail.value;
    var elem = document.getElementById("content");
    
    elem.classList.remove("hide");

    if (val && val.trim() !== '') {
      this.items = this.items.filter(term => {
        return term.title.toLowerCase().indexOf(val.trim().toLowerCase()) > -1;
      })
    }

    //console.log(this.allItems[0]);
    //if (this.items == [{title: "KLCC", icon: "KLCC"}]){alert("KLCC")}
  }

  //call this function when bg is click, add hide to content
  clickChange(ev : CustomEvent) {
    var elem = document.getElementById("content");
    elem.classList.add("hide");
  }

  click_item(item: object){
    console.log(item);
    alert(this.items);  
  }

  navigate(){
    this.router.navigate(['/shop_search'])
  }

  
}
