# -*- coding: utf-8 -*-
from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from ID_animations import *


additional_scripts = [


#-## List management (no dependency)
("list_clear", [
## The list's zero slot holds the number of current items in it
# script_list_clear
# Clears all items from the list
# INPUT: arg1 - list no
# OUTPUT: none
  (store_script_param, ":list_no", 1),
  (troop_get_slot, ":num_elements", ":list_no", 0),
  (val_add, ":num_elements", 1),
  (try_for_range, ":slot", 1, ":num_elements"),
    (troop_set_slot, ":list_no", ":slot", 0),
  (try_end),
  (troop_set_slot, ":list_no", 0, 0), # Reset number of elements
]),
("list_at",[
# Returns the value at the specified index, 0 if index is invalid
# INPUT: arg1 - list no; arg2 - index
# OUTPUT: arg1 - value
  (store_script_param, ":list_no", 1),
  (store_script_param, ":index", 2),
  
  (troop_get_slot, ":num_elements", ":list_no", 0),
  (assign, reg1, 0),
  (try_begin),
    (ge, ":index", 1),
    (le, ":index", ":num_elements"),
      (troop_get_slot, reg1, ":list_no", ":index"),
  (try_end),
]),
("list_at_nc",[
# Returns the value at the specified index; IT DOES NOT CHECK FOR INDEX VALIDITY
# INPUT: arg1 - list no; arg2 - index
# OUTPUT: arg1 - value
  (store_script_param, ":list_no", 1),
  (store_script_param, ":index", 2),
  
  (troop_get_slot, reg1, ":list_no", ":index"),
]),
("list_set", [
# script_list_set
# Sets an item's, at the specified index
# INPUT: arg1 - list no; arg2 - the value which we will set, arg3 - where we want it (ONE-BASED!)
# OUTPUT: none
  (store_script_param, ":list_no", 1),
  (store_script_param, ":value", 2),
  (store_script_param, ":index", 3),
  (troop_get_slot, ":num_elements", ":list_no", 0),
  (try_begin),
    (ge, ":index", 1),
    (le, ":index", ":num_elements"),
      (troop_set_slot, ":list_no", ":index", ":value"),
  (try_end),
]),
("list_add", [
# script_list_add
# Appends an item to the list
# INPUT: arg1 - list no; arg2 - the value which we will add to the list
# OUTPUT: none
  (store_script_param, ":list_no", 1),
  (store_script_param, ":value", 2),
  (troop_get_slot, ":num_elements", ":list_no", 0),
  (val_add, ":num_elements", 1),
  (troop_set_slot, ":list_no", ":num_elements", ":value"),
  (troop_set_slot, ":list_no", 0, ":num_elements"),
]),
("list_add_at", [
# script_list_add_at
# Appends an item to the list, at the specified index
# INPUT: arg1 - list no; arg2 - the value which we will add to the list, arg3 - where we want it (ONE-BASED!)
# OUTPUT: none
  (store_script_param, ":list_no", 1),
  (store_script_param, ":value", 2),
  (store_script_param, ":index", 3),
  (troop_get_slot, ":num_elements", ":list_no", 0),
  (val_add, ":num_elements", 1),
  (try_begin),
    (this_or_next|gt, ":index", ":num_elements"),
    (le, ":index", 0),
      (assign, ":index", ":num_elements"),
  (try_end),
  (try_for_range_backwards, ":slot", ":index", ":num_elements"),
    (store_add, ":target", ":slot", 1),
    (troop_get_slot, ":val", ":list_no", ":slot"),
    (troop_set_slot, ":list_no", ":target", ":val"),
  (try_end),
  (troop_set_slot, ":list_no", ":index", ":value"),
  (troop_set_slot, ":list_no", 0, ":num_elements"),
]),
("list_remove", [
# script_list_remove
# Removes the last item from the list
# INPUT: arg1 - list no
# OUTPUT: none
  (store_script_param, ":list_no", 1),
  (troop_get_slot, ":num_elements", ":list_no", 0),
  (try_begin),
    (ge, ":num_elements", 1),
      (troop_set_slot, ":list_no", ":num_elements", 0),
      (val_sub, ":num_elements", 1),
      (troop_set_slot, ":list_no", 0, ":num_elements"),
  (try_end),
]),
("list_remove_at", [
# script_list_remove_at
# Removes an item from the list, at the specified index
# INPUT: arg1 - list no; arg2 - the index we'll remove from (ONE-BASED!)
# OUTPUT: none
  (store_script_param, ":list_no", 1),
  (store_script_param, ":index", 2),
  (troop_get_slot, ":num_elements", ":list_no", 0),
  (try_begin),
    (this_or_next|gt, ":index", ":num_elements"),
    (le, ":index", 0),
    (assign, ":index", ":num_elements"),
  (try_end),
  (store_add, ":end", ":num_elements", 1),
  (val_sub, ":num_elements", 1),
  (store_add, ":start", ":index", 1),
  (try_for_range, ":slot", ":start", ":end"),
    (troop_get_slot, ":val", ":list_no", ":slot"),
    (troop_set_slot, ":list_no", ":index", ":val"),
    (val_add, ":index", 1),
  (try_end),
  (troop_set_slot, ":list_no", 0, ":num_elements"),
]),
("list_remove_val", [
# script_list_remove_val
# Removes a value from the list
# INPUT: arg1 - list no; arg2 - the value we'll remove
# OUTPUT: none
  (store_script_param, ":list_no", 1),
  (store_script_param, ":value", 2),
  (call_script, "script_list_index_of", ":list_no", ":value"),
  (try_begin),
    (neq, reg1, -1),
    (assign, ":index", reg1),
    (troop_get_slot, ":num_elements", ":list_no", 0),
    (try_begin),
      (gt, ":index", ":num_elements"),
      (assign, ":index", ":num_elements"),
    (try_end),
    (store_add, ":end", ":num_elements", 1),
    (val_sub, ":num_elements", 1),
    (store_add, ":start", ":index", 1),
    (try_for_range, ":slot", ":start", ":end"),
      (troop_get_slot, ":val", ":list_no", ":slot"),
      (troop_set_slot, ":list_no", ":index", ":val"),
      (val_add, ":index", 1),
    (try_end),
    (troop_set_slot, ":list_no", 0, ":num_elements"),
  (try_end),
]),
("list_index_of", [
# script_list_index_of
# Returns the index of something from the list
# INPUT: arg1 - list no; arg2 - the value we're looking for
# OUTPUT: reg1 - the index (-1 if not found)
  (store_script_param, ":list_no", 1),
  (store_script_param, ":val", 2),
  (assign, ":index", -1),
  (troop_get_slot, ":num_elements", ":list_no", 0),
  (val_add, ":num_elements", 1),
  (try_for_range, ":slot", 1, ":num_elements"),
    (troop_slot_eq, ":list_no", ":slot", ":val"),
    (assign, ":index", ":slot"),
    (assign, ":num_elements", 0),
  (try_end),
  (assign, reg1, ":index"),
]),
("list_count", [
# script_list_count
# Returns how many items there are in the list
# INPUT: arg1 - list no
# OUTPUT: reg1 - the list's length
  (store_script_param, ":list_no", 1),
  (troop_get_slot, reg1, ":list_no", 0),
]),
("list_last", [
# script_list_last
# Returns the last element of the list
# INPUT: arg1 - list no
# OUTPUT: reg1 - last value
  (store_script_param, ":list_no", 1),
  (troop_get_slot, ":num_elements", ":list_no", 0),
  (troop_get_slot, reg1, ":list_no", ":num_elements"),
]),
("list_random", [
  # script_list_random
  # Returns a random element from the list, along with its index
  # INPUT: arg1 - list no
  # OUTPUT: reg1 - the value of the item, reg2 - its index
  (store_script_param, ":list_no", 1),
  (troop_get_slot, ":num_elements", ":list_no", 0),
  (val_add, ":num_elements", 1),
  (store_random_in_range, reg2, 1, ":num_elements"),
  (troop_get_slot, reg1, ":list_no", reg2),
]),
#-## List management end
    
#-## Broadcast utility (no dependency)
("broadcast_string",[

  (store_script_param_1, ":event_no"),
  (store_script_param_2, ":string_reg_no"),
  
  (str_store_string_reg, s0, ":string_reg_no"),
  
  (try_for_range, ":c_player", 1, 250),
    (player_is_active, ":c_player"),
    (multiplayer_send_string_to_player, ":c_player", ":event_no", s0),
  (try_end),
]),      
("broadcast_event",[
  (store_script_param_1, ":event_no"),

  (try_for_range, ":c_player", 1, 250),
    (player_is_active, ":c_player"),
    (multiplayer_send_message_to_player, ":c_player", ":event_no"),
  (try_end),
]),      
("broadcast_int",[
  (store_script_param_1, ":event_no"),
  (store_script_param_2, ":val_1"),

  (try_for_range, ":c_player", 1, 250),
    (player_is_active, ":c_player"),
    (multiplayer_send_int_to_player, ":c_player", ":event_no", ":val_1"),
  (try_end),
]), 
("broadcast_2_int",[
  (store_script_param_1, ":event_no"),
  (store_script_param_2, ":val_1"),
  (store_script_param, ":val_2", 3),

  (try_for_range, ":c_player", 1, 250),
    (player_is_active, ":c_player"),
    (multiplayer_send_2_int_to_player, ":c_player", ":event_no", ":val_1", ":val_2"),
  (try_end),
]),  
("broadcast_3_int",[
  (store_script_param_1, ":event_no"),
  (store_script_param_2, ":val_1"),
  (store_script_param, ":val_2", 3),
  (store_script_param, ":val_3", 4),

  (try_for_range, ":c_player", 1, 250),
    (player_is_active, ":c_player"),
    (multiplayer_send_3_int_to_player, ":c_player", ":event_no", ":val_1", ":val_2", ":val_3"),
  (try_end),
]),  
("broadcast_4_int",[
  (store_script_param_1, ":event_no"),
  (store_script_param_2, ":val_1"),
  (store_script_param, ":val_2", 3),
  (store_script_param, ":val_3", 4),
  (store_script_param, ":val_4", 5),

  (try_for_range, ":c_player", 1, 250),
    (player_is_active, ":c_player"),
    (multiplayer_send_4_int_to_player, ":c_player", ":event_no", ":val_1", ":val_2", ":val_3", ":val_4"),
  (try_end),
]),

("init_callbacks",[
  (assign, "$callbacks_root_p", 0),
]),
("register_cb",[
  (store_script_param_1, ":miliseconds"),
  (store_script_param_2, ":script_no"),
  (store_script_param, ":num_params", 3),
  
  (store_mission_timer_c_msec, ":c_milis"),
  (store_add, ":cb_time", ":c_milis", ":miliseconds"),
  
 
  (call_script, "script_alloc", 14), ## 2 pointers + time + script + 10 params = 14 vars
  (assign, ":new_node", reg0),
  
  (call_script, "script_v_set", ":new_node", 0, 0),# prev p
  (call_script, "script_v_set", ":new_node", 1, 0),# next p
  (call_script, "script_v_set", ":new_node", 2, ":cb_time"),    # time
  (call_script, "script_v_set", ":new_node", 3, ":script_no"),  # script no
  
  
  (val_clamp, ":num_params", 0, 11),
  (assign, ":c_script_param", 4),
  (store_add, ":end_cond", ":num_params", 4),
  (assign, ":c_i", 4),
  (try_for_range, ":c_script_param", 4, ":end_cond"),
    (store_script_param, ":param_value", ":c_script_param"),
    (call_script, "script_v_set", ":new_node", ":c_i", ":param_value"),  # params
    (val_add, ":c_i", 1),
  (try_end),
  
  (try_for_range, ":i", ":c_i", 11),
    (call_script, "script_v_set", ":new_node", ":i", 0),  # params
  (try_end),
  
  ### node is constructed
  
  (assign, reg10, ":miliseconds"),
  
  (try_begin),
    (eq, "$callbacks_root_p", 0),
      (assign, "$callbacks_root_p", ":new_node"),
    # (display_message, "@{reg10} - 1"),
  (else_try),
    (assign, ":end_cond", 9999),
    (assign, ":c_node", "$callbacks_root_p"),
    (try_for_range, ":unused", 0, ":end_cond"),
      (call_script, "script_v_get", ":c_node", 1),
      (assign, ":next_p", reg0),
      (call_script, "script_v_get", ":c_node", 2),
      (try_begin),
        (ge, reg0, ":cb_time"),
        # (display_message, "@{reg10} - 2"),
        (try_begin),
          (call_script, "script_v_get", ":c_node", 0), # get the prev p
          (try_begin),
            (neq, reg0, 0),
            # (display_message, "@{reg10} - 3"),
              (call_script, "script_v_set", reg0, 1, ":new_node"), # set prev p next's p to the new node
              (call_script, "script_v_set", ":new_node", 0, reg0),
          (else_try),
            (assign, "$callbacks_root_p", ":new_node"),
              # (display_message, "@{reg10} - 4"),
          (try_end),
          (call_script, "script_v_set", ":c_node", 0, ":new_node"), # set next p prev's p to new node
          (call_script, "script_v_set", ":new_node", 1, ":c_node"),
        (try_end),
        (assign, ":end_cond", 0),
      (else_try),
        (eq, ":next_p", 0),
          # (display_message, "@{reg10} - 6"),
          (call_script, "script_v_set", ":c_node", 1, ":new_node"),
          (call_script, "script_v_set", ":new_node", 0, ":c_node"),
          (assign, ":end_cond", 0),
      (try_end),
    # (display_message, "@{reg10} - 7"),
      (assign, ":c_node", ":next_p"),
    (try_end),
  (try_end),
]),
("process_callbacks",[
  (try_begin),  
    (neq, "$callbacks_root_p", 0),
    (store_mission_timer_c_msec, ":c_milis"),
    (assign, ":c_node", "$callbacks_root_p"),
    (assign, ":end_cond", 9999),
    (try_for_range, ":unused", 0, ":end_cond"),
      (call_script, "script_v_get", ":c_node", 2),
      (try_begin),
        (ge, ":c_milis", reg0),
        ## execute script
        (call_script, "script_v_get", ":c_node", 3),
        (assign, ":script_no", reg0),
        (call_script, "script_v_get", ":c_node", 4),
        (assign, ":param_1", reg0),
        (call_script, "script_v_get", ":c_node", 5),
        (assign, ":param_2", reg0),
        (call_script, "script_v_get", ":c_node", 6),
        (assign, ":param_3", reg0),
        (call_script, "script_v_get", ":c_node", 7),
        (assign, ":param_4", reg0),
        (call_script, "script_v_get", ":c_node", 8),
        (assign, ":param_5", reg0),
        (call_script, "script_v_get", ":c_node", 9),
        (assign, ":param_6", reg0),
        (call_script, "script_v_get", ":c_node", 10),
        (assign, ":param_7", reg0),
        (call_script, "script_v_get", ":c_node", 11),
        (assign, ":param_8", reg0),
        (call_script, "script_v_get", ":c_node", 12),
        (assign, ":param_9", reg0),
        (call_script, "script_v_get", ":c_node", 13),
        (assign, ":param_10", reg0),
        
        (call_script, "script_v_get", ":c_node", 1), # get next p
        (assign, ":next_p", reg0),
        (try_begin),
          (neq, ":next_p", 0),
            (call_script, "script_v_set", ":next_p", 0, 0),  # set next node's prev pointer to null
            (assign, "$callbacks_root_p", ":next_p"),
        (else_try),
          (assign, "$callbacks_root_p", 0),
          (assign, ":end_cond", 0),
        (try_end),
        (call_script, "script_free", ":c_node"),
        (assign, ":c_node", ":next_p"),
        
        (call_script, ":script_no", ":param_1", ":param_2", ":param_3", ":param_4", ":param_5", ":param_6", ":param_7", ":param_8", ":param_9", ":param_10"),
      (else_try),
        (assign, ":end_cond", 0),
      (try_end),
    (try_end),
  (try_end),
]),
#-## Timed callbacks end


#-## dynamic memory (list system dependent!!!)
("init_memory_management", [
  (troop_set_slot, "trp_dynamic_memory", 0, 0),
  
  (call_script, "script_list_clear", "trp_list_free_dynamic_memory_pointers_indexes"),
  (call_script, "script_list_clear", "trp_list_free_dynamic_memory_pointers_sizes"),
  (call_script, "script_list_clear", "trp_list_allocated_dynamic_memory_pointers_indexes"),
  (call_script, "script_list_clear", "trp_list_allocated_dynamic_memory_pointers_sizes"),
]),
("alloc", [
## This script allocates the specified ammount of variables
# script_alloc
# Allocates memory
# INPUT: arg1 - num variables to allocate
# OUTPUT: reg0 - pointer to the firs variable
  (store_script_param_1, ":block_size"),

  (troop_get_slot, ":num_free_pointers", "trp_list_free_dynamic_memory_pointers_sizes", 0),
  
  (assign, ":found", 0),
  (try_begin),
    (neq, ":num_free_pointers", 0),
    (val_add, ":num_free_pointers", 1),
    (try_for_range, ":i_pointer_index", 1, ":num_free_pointers"),
      (troop_slot_ge, "trp_list_free_dynamic_memory_pointers_sizes", ":i_pointer_index", ":block_size"),
      # we've found our pointer; remove it from the list and return it
      (assign, ":found", 1),
      (assign, ":num_free_pointers", 0),
      
      
      (call_script, "script_list_at_nc", "trp_list_free_dynamic_memory_pointers_sizes", ":i_pointer_index"),
      (call_script, "script_list_add", "trp_list_allocated_dynamic_memory_pointers_sizes", reg1),
      
      (call_script, "script_list_at_nc", "trp_list_free_dynamic_memory_pointers_indexes", ":i_pointer_index"),
      (assign, reg0, reg1),
      (call_script, "script_list_add", "trp_list_allocated_dynamic_memory_pointers_indexes", reg1),
      
      (call_script, "script_list_remove_at", "trp_list_free_dynamic_memory_pointers_indexes", ":i_pointer_index"),
      (call_script, "script_list_remove_at", "trp_list_free_dynamic_memory_pointers_sizes", ":i_pointer_index"),
    (try_end),
  (try_end),
  
  (try_begin),
    (eq, ":found", 0),
      (troop_get_slot, ":pointer_to_end", "trp_dynamic_memory", 0),
      (store_add, reg0, ":pointer_to_end", 1),
      (call_script, "script_list_add", "trp_list_allocated_dynamic_memory_pointers_indexes", reg0),
      (call_script, "script_list_add", "trp_list_allocated_dynamic_memory_pointers_sizes", ":block_size"),
      (val_add, ":pointer_to_end", ":block_size"),
      (troop_set_slot, "trp_dynamic_memory", 0, ":pointer_to_end"),
  (try_end),
]),
("free", [
## This script frees allocated memory block
# script_free
# Frees memory
# INPUT: arg1 - pointer to block of variables that needs to be freed
# OUTPUT: none
  (store_script_param_1, ":block_pointer"),

  (call_script, "script_list_index_of", "trp_list_allocated_dynamic_memory_pointers_indexes", ":block_pointer"),
  (assign, ":p_index", reg1),
  (try_begin),
    (eq, ":p_index", -1),
      ### ERROR! invalid pointer
  (else_try),
    (call_script, "script_list_add", "trp_list_free_dynamic_memory_pointers_indexes", ":block_pointer"),
    
    (call_script, "script_list_at_nc", "trp_list_allocated_dynamic_memory_pointers_sizes", ":p_index"),
    (call_script, "script_list_add", "trp_list_free_dynamic_memory_pointers_sizes", reg1),
    
    (call_script, "script_list_remove_at", "trp_list_allocated_dynamic_memory_pointers_indexes", ":p_index"),
    (call_script, "script_list_remove_at", "trp_list_allocated_dynamic_memory_pointers_sizes", ":p_index"),
  (try_end),
]),

("get",[
## This script returns the value pointed to by the pointer
# script_get
# Return value being pointed at
# INPUT: arg1 - pointer
# OUTPUT: reg0 - value pointed by the pointer
  (store_script_param_1, ":pointer"),

  (troop_get_slot, reg0, "trp_dynamic_memory", ":pointer"),
]),
("set",[
## This script sets the value of the pointed object
# script_set
# Sets value
# INPUT: arg1 - pointer; arg2 - value to set
# OUTPUT: none
  (store_script_param_1, ":pointer"),
  (store_script_param_2, ":value"),
  (try_begin),
    (neq, ":pointer", 0),
    (troop_set_slot, "trp_dynamic_memory", ":pointer", ":value"),
  (try_end),
]),

("v_get",[
## This script returns the value pointed to by the pointer, at a specific index
# script_v_get
# Return value being pointed at
# INPUT: arg1 - pointer; arg2 - index
# OUTPUT: reg0 - value pointed by the pointer
  (store_script_param_1, ":pointer"),
  (store_script_param_2, ":index"),
  (val_add, ":pointer", ":index"),
  (troop_get_slot, reg0, "trp_dynamic_memory", ":pointer"),
]),
("v_set",[
## This script sets the value of the pointed object, at a specific index
# script_v_set
# Sets value
# INPUT: arg1 - pointer; arg2 - index; arg3 - value to set
# OUTPUT: none
  (store_script_param_1, ":pointer"),
  (store_script_param_2, ":index"),
  (store_script_param, ":value", 3),
  (val_add, ":pointer", ":index"),
  (try_begin),
    (neq, ":pointer", 0),
    (troop_set_slot, "trp_dynamic_memory", ":pointer", ":value"),
  (try_end),
]),
#-## dynamic memory end


 # script_point_y_toward_position by motomataru
  # Input: from position, to position
  # Output: reg0 distance in cm
  # Basically, points the first position at the second, so then simple move_y will move back and forth and move_x side to side
("point_y_toward_position", [
	(store_script_param, ":from_position", 1),
	(store_script_param, ":to_position", 2),
	(assign, ":save_fpm", 1),
	(convert_to_fixed_point, ":save_fpm"),
	(set_fixed_point_multiplier, 100),  #to match cm returned by get_distance_between_positions
	
	#remove current rotation
	(position_get_x, ":from_x", ":from_position"),
	(position_get_y, ":from_y", ":from_position"),
	(position_get_z, ":from_z", ":from_position"),
	(init_position, ":from_position"),
	(position_set_x, ":from_position", ":from_x"),
	(position_set_y, ":from_position", ":from_y"),
	(position_set_z, ":from_position", ":from_z"),
	
	#horizontal rotation
	(position_get_x, ":change_in_x", ":to_position"),
	(val_sub, ":change_in_x", ":from_x"),
	(position_get_y, ":change_in_y", ":to_position"),
	(val_sub, ":change_in_y", ":from_y"),
	
	(try_begin),
		(this_or_next|neq, ":change_in_y", 0),
		(neq, ":change_in_x", 0),
		(store_atan2, ":theta", ":change_in_y", ":change_in_x"),
		(assign, ":ninety", 90),
		(convert_to_fixed_point, ":ninety"),
		(val_sub, ":theta", ":ninety"),	#point Y axis at to position
		(position_rotate_z_floating, ":from_position", ":theta"),
	(try_end),
	
	#vertical rotation
	(get_distance_between_positions, ":distance_between", ":from_position", ":to_position"),
	(try_begin),
		(gt, ":distance_between", 0),
		(position_get_z, ":dist_z_to_sine", ":to_position"),
		(val_sub, ":dist_z_to_sine", ":from_z"),
		(val_div, ":dist_z_to_sine", ":distance_between"),
		(store_asin, ":theta", ":dist_z_to_sine"),
		(position_rotate_x_floating, ":from_position", ":theta"),
	(try_end),
	
	(assign, reg0, ":distance_between"),
	(set_fixed_point_multiplier, ":save_fpm"),
  ]),



]