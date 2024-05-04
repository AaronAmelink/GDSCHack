using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using System;
using System.IO;

public class artScript : MonoBehaviour
{
    public float height;
    public float width;

    public string imagePath;


    // Start is called before the first frame update
    public void Start()
    {
        // Create a texture. Texture size does not matter, since
        // LoadImage will replace with the size of the incoming image.
        Texture2D tex = new Texture2D(2, 2);
        byte[] imageData = File.ReadAllBytes(imagePath);
        ImageConversion.LoadImage(tex, imageData);
        GetComponent<Renderer>().material.mainTexture = tex;

        float accHeight = (float)(height*0.1);
        float accWidth = (float)(width*0.1);
        transform.localScale = new Vector3(accWidth, 1, accHeight); //the z is the height...not y. Data size is in cm, unit measurement is in m

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
