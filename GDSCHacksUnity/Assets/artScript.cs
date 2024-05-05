using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using System;
using System.IO;
using TMPro;

public class artScript : MonoBehaviour
{


    // Start is called before the first frame update
    public void Start()
    {
        // Create a texture. Texture size does not matter, since
        // LoadImage will replace with the size of the incoming image.
         //the z is the height...not y. Data size is in cm, unit measurement is in m

    }
    public float accHeight;
    public float accWidth;
    public GameObject plane;
    public TextMeshPro title;
    public TextMeshPro artist;
    public TextMeshPro period;
    public GameObject text;


    public void loadData(string fileName, float widthCM, float heightCM, string t, string a, string p, string galleryName)
    {
        Texture2D tex = new Texture2D(2, 2);
        byte[] imageData = File.ReadAllBytes(Application.dataPath + "/Art/"+ galleryName + "/Pictures/" + fileName);
        ImageConversion.LoadImage(tex, imageData);
        plane.GetComponent<Renderer>().material.mainTexture = tex;
        title.text = t;
        artist.text = a;
        period.text = p;

        if (heightCM != 0)
        {
            accHeight = heightCM * 0.001f;
            accWidth = widthCM * 0.001f;
            plane.transform.localScale = new Vector3(accWidth, 0.5f, accHeight);
            text.transform.localScale = new Vector3(accWidth, accWidth, 1);
        }
        else
        {
            accHeight = 0.1f;
            accWidth = 0.1f;
            plane.transform.localScale = new Vector3(plane.transform.localScale.x * 0.1f, plane.transform.localScale.y * 0.1f, plane.transform.localScale.z * 0.1f); 
            text.transform.localScale = new Vector3(0.1f, 0.1f, 1);
        }
        
        text.transform.localPosition = new Vector3(accWidth*10 / 2, -accHeight*10 / 2, -0.2f);

        if (text.transform.position.y < -1)
        {
            text.transform.localPosition = new Vector3(text.transform.localPosition.x, -0.7f, text.transform.localPosition.z);
        }
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
