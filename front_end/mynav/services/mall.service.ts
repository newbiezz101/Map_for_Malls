import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MallService {
  get_mall_url = 'http://localhost:3000/api/getMall';
  post_mall_url = 'http://localhost:3000/api/postMall';

  constructor(private http: HttpClient) { }

  getMall(){
    console.log("Api is working fine");
    return this.http.get(this.get_mall_url);
  }

  postMall(mall){
    var headers = new HttpHeaders();
    headers.append('Content-Type', 'application/json');
    return this.http.post(this.post_mall_url, mall, {headers:headers});
  }
}
