import { Component } from '@angular/core';

@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent {
    
  eventData=[
    {Title: "PokerBaazi presents",Year:"2023",indbID:"9.5",Type:"comedy",Poster:"https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:ote-VGh1LCAzIEF1Zw%3D%3D,ots-29,otc-FFFFFF,oy-612,ox-24:q-80/et00359503-kjsjfumebw-portrait.jpg"},
    {Title: "Anubhav Singh Bassi",Year:"2000",indbID:"8.5",Type:"comedy",Poster:"https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:ote-V2VkLCAyNiBKdWwgb253YXJkcw%3D%3D,ots-29,otc-FFFFFF,oy-612,ox-24:q-80/et00355125-mqmycvxlpm-portrait.jpg"},
    {Title: "Gaurav Gupta",Year:"1996",indbID:"7.5",Type:"comedy",Poster:"https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:ote-U3VuLCAyMCBBdWc%3D,ots-29,otc-FFFFFF,oy-612,ox-24:q-80/et00321882-mkazcxcdwt-portrait.jpg"},
    {Title: "Harshal Gujral",Year:"2019",indbID:"6.5",Type:"comedy",Poster:"https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:ote-U2F0LCAyOSBKdWw%3D,ots-29,otc-FFFFFF,oy-612,ox-24:q-80/et00363306-dzyuhfvnag-portrait.jpg"},
    {Title: "Vipul Goyal",Year:"2000",indbID:"5.5",Type:"comedy",Poster:"https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:ote-V2VkLCAyNiBKdWwgb253YXJkcw%3D%3D,ots-29,otc-FFFFFF,oy-612,ox-24:q-80/et00319088-kmszandhlz-portrait.jpg"},
    {Title: "Kachha Ghada",Year:"2025",indbID:"4.5",Type:"comedy",Poster:"https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:ote-U2F0LCAzMCBTZXA%3D,ots-29,otc-FFFFFF,oy-612,ox-24:q-80/et00361501-zhsqjatmkp-portrait.jpg"},
    {Title: "Madhur Virli",Year:"2020",indbID:"3.5",Type:"comedy",Poster:"https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:ote-U2F0LCAyOSBKdWw%3D,ots-29,otc-FFFFFF,oy-612,ox-24:q-80/et00363060-tujwhajrdf-portrait.jpg"},
    {Title: "Gaurav Kapoor",Year:"2022",indbID:"9.2",Type:"comedy",Poster:"https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:ote-U3VuLCAyMyBKdWw%3D,ots-29,otc-FFFFFF,oy-612,ox-24:q-80/et00363278-bcpdfeucel-portrait.jpg"},
    {Title: "Pria Malik",Year:"2024",indbID:"9.1",Type:"comedy",Poster:"https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:ote-VGh1LCAyNyBKdWwgb253YXJkcw%3D%3D,ots-29,otc-FFFFFF,oy-612,ox-24:q-80/et00331112-fwyjvasbuy-portrait.jpg"},
  ]
}
