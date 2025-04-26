import io
import base64

def extract_image(data_dict: dict) -> list:
    extracted_images = []
    for key, value in data_dict.items():
        if key.startswith('image_') and value is not None:
            extracted_images.append(value)
    return extracted_images


def image_to_base64(image):
    img_buffer = io.BytesIO()
    image.save(img_buffer, format="PNG")
    byte_data = img_buffer.getvalue()
    base64_string = base64.b64encode(byte_data).decode()
    return base64_string


def extract_image_list(images, visual_prompting: callable, model = "gpt"):
    if visual_prompting is None:
        return images 

    if model == "gpt":
        image_list = []
        for img in images:
            image_list.append(img)
            image_list.append(visual_prompting(img, 4, 4))
        images = [image_to_base64(x) for x in image_list]
        images_type_list = [{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{k}"}} for k in images]


    elif model == "opus":
        image_list = []
        for img in images:
            image_list.append(img)
            image_list.append(visual_prompting(img, 4, 4))
        images_type_list = [{
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": image_to_base64(image),
                            },
                        } for image in image_list]



    else:
        raise ValueError("Model type doesn't support, please make a selection over `gpt` or `opus`")
    
    return images_type_list
    