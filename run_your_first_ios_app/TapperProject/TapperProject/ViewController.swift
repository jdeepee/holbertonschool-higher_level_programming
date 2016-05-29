//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var taps_done: Int = 0
    var taps_requested: Int = 0
    
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var button_coin: UIButton!
    
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var button_play: UIImageView!

    @IBAction func clickPlayButton(sender: AnyObject) {
        if self.textfield_number != nil && self.textfield_number.text != "" {
            if (Int(self.textfield_number.text!) <= 0){
            } else {
                self.textfield_number.text = self.textfield_number.text
                taps_requested = Int(self.textfield_number.text!)!
                initGame()
            }
        }
    }
    
    @IBAction func clickCoinButton(sender: AnyObject){
        print("Tap!")
        taps_done += 1
        label_taps.text = String(taps_done) + " Taps"
        
        if taps_done < taps_requested{
        } else if taps_done >= taps_requested {
            resetGame()
        }
    }
    
    func initGame() {
        image_tapper.hidden = true
        button_play.hidden = true
        textfield_number.hidden = true
        
        label_taps.hidden = false
        button_coin.hidden = false
        
        taps_done = 0
        label_taps.text = "0 Taps"
    }
    
    func resetGame() {
        label_taps.hidden = true
        button_coin.hidden = true
        
        image_tapper.hidden = false
        button_play.hidden = false
        textfield_number.hidden = false
        
        taps_requested = 0
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}

