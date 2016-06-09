//
//  TechCompanyDetailViewController.swift
//  TechCompanies
//
//  Created by Joshua Parkin on 09/06/2016.
//  Copyright © 2016 Joshua Parkin. All rights reserved.
//

import UIKit

class TechCompanyDetailViewController: UIViewController {
    
    @IBOutlet weak var label_entity: UILabel!
    @IBOutlet weak var image_entity: UIImageView!
    
    var entity:Entity!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        if self.entity != nil {
            self.title = entity.name
            self.label_entity.text = entity.town
            self.image_entity.image = UIImage(imageLiteral: entity.imageName)
            self.image_entity.contentMode = .ScaleAspectFit
        }
        // Do any additional setup after loading the view.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

}
